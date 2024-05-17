document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('file-input');
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        
        console.log('Файл загружен:', file);
        
        document.getElementById('transcript').value = "Пример расшифровки текста для загруженного файла.";
    } else {
        alert('Пожалуйста, выберите файл.');
    }
});
