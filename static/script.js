document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("upload-form");
    const fileInput = document.getElementById("file-input");
    const outputDiv = document.getElementById("output");

    form.onsubmit = async function (e) {
        e.preventDefault();
        outputDiv.innerHTML = "Processing...";
        const file = fileInput.files[0];
        if (!file) return;

        // Display image
        const reader = new FileReader();
        reader.onload = function (event) {
            outputDiv.innerHTML = `<h3>Uploaded Image</h3>
                <img src="${event.target.result}" alt="Uploaded Image"/>`;
        };
        reader.readAsDataURL(file);

        // Prepare form data
        const formData = new FormData();
        formData.append("file", file);

        // Call API
        const response = await fetch("/extract-text/", {
            method: "POST",
            body: formData
        });
        const result = await response.json();

        // Display extracted text
        outputDiv.innerHTML += `<h3>Extracted Text</h3><pre>${result.extracted_text}</pre>`;
    };
});
