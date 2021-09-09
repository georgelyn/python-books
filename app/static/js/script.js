window.onload = function () {
  const form = document.getElementById('book-form');
  if (form) {
    form.addEventListener('submit', validateFields);
  }
};

const validateFields = (event) => {
  event.preventDefault();
  const form = document.getElementById('book-form');
  const nameInput = document.getElementById('name');
  const authorInput = document.getElementById('author');

  if (nameInput.value.trim() !== '' && authorInput.value.trim() !== '') {
    form.submit();
  }

  if (nameInput.value.trim() === '') {
    alert('The name cannot be empty.');
    nameInput.focus();
    return false;
  } else if (authorInput.value.trim() === '') {
    alert('The author cannot be empty.');
    authorInput.focus();
    return false;
  }
};

const previewPicture = () => {
  const fileExplorer = document.getElementById('file-explorer');
  fileExplorer.click();

  fileExplorer.addEventListener('change', function () {
    if (this.value) {
      const imgPreview = document.getElementById('img-preview');
      const file = fileExplorer.files[0];
      imgPreview.src = URL.createObjectURL(file);
      imgPreview.onload = function () {
        URL.revokeObjectURL(this.src);
      };
    }
  });
};

const removePicture = () => {
  const imgPreview = document.getElementById('img-preview');
  imgPreview.src = '';
};
