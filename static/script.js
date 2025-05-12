document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("upload-form");
    const fileInput = document.getElementById("file-input");
    const outputDiv = document.getElementById("output");
    const replacementForm = document.getElementById("replacement-form");
    const revisedAdDiv = document.getElementById("revised-ad");

    // Helper function to create a textarea
    function createTextarea({ name, value = "", placeholder = "", disabled = false }) {
        const textarea = document.createElement("textarea");
        textarea.name = name;
        textarea.value = value;
        textarea.placeholder = placeholder;
        textarea.disabled = disabled;
        textarea.style.marginBottom = "10px";
        return textarea;
    }

    // Function to handle form submission for text extraction
    async function handleTextExtraction(e) {
        e.preventDefault();
        outputDiv.innerHTML = "Processing...";
        const file = fileInput.files[0];
        if (!file) {
            console.error("No file selected");
            return;
        }

        // Display uploaded image
        const reader = new FileReader();
        reader.onload = (event) => {
            outputDiv.innerHTML = `<h3>Uploaded Image</h3>
                <img src="${event.target.result}" alt="Uploaded Image"/>`;
        };
        reader.readAsDataURL(file);

        // Prepare form data and call the API
        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch("/extract-text/", {
            method: "POST",
            body: formData,
        });
        const result = await response.json();
        const ocrTexts = result.extracted_text;

        displayReplacementForm(ocrTexts, file);
    }

    // Function to display the replacement form
    function displayReplacementForm(ocrTexts, file) {
        replacementForm.innerHTML = ""; // Clear previous content

        ocrTexts.forEach((aText, index) => {
            // Create and append original (disabled) textarea
            const originalTextArea = createTextarea({
                name: `original_text_${index}`,
                value: aText.text,
                disabled: true,
            });
            replacementForm.appendChild(originalTextArea);

            // Create and append editable replacement textarea
            const replacementTextArea = createTextarea({
                name: `replacement_text_${index}`,
                placeholder: "Enter replacement text here...",
            });
            replacementForm.appendChild(replacementTextArea);

            // Add a line break
            replacementForm.appendChild(document.createElement("br"));
        });

        // Add a submit button to the form
        const submitButton = document.createElement("button");
        submitButton.type = "submit";
        submitButton.textContent = "Submit Replacements";
        replacementForm.appendChild(submitButton);

        // Attach event listener for replacement form submission
        replacementForm.onsubmit = (e) => handleReplacementSubmission(e, ocrTexts, file);
    }

    // Function to handle replacement form submission
    async function handleReplacementSubmission(e, ocrTexts, file) {
        e.preventDefault();

        const replacementData = new FormData(replacementForm);
        const replacements = ocrTexts.map((text, index) => ({
            ...text,
            replacement: replacementData.get(`replacement_text_${index}`),
        }));

        // Prepare form data for API call
        const replacementFormData = new FormData();
        replacementFormData.append("file", file, file.name);
        replacementFormData.append("replacements", JSON.stringify(replacements));

        // Call API to process replacements
        const response = await fetch("/replace-image-text/", {
            method: "POST",
            body: replacementFormData,
        });
        const result = await response.json();

        // Display the processed image
        revisedAdDiv.innerHTML = `<h3>Processed Image</h3>
            <img src="${result.image_after_replacements}" alt="Processed Image"/>`;
    }

    // Attach event listener for the main form submission
    form.onsubmit = handleTextExtraction;
});
