document.getElementById('upload-btn').addEventListener('click', function () {
    let fileInput = document.getElementById('file-upload');
    let file = fileInput.files[0];

    if (!file) {
        alert('Please select a file to upload.');
        return;
    }

    let formData = new FormData();
    formData.append('file', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction) {
            document.getElementById('prediction-result').innerText = 'Prediction: ' + data.prediction;
        } else {
            document.getElementById('prediction-result').innerText = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        document.getElementById('prediction-result').innerText = 'Error: ' + error.message;
    });
});
