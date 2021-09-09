window.onload = function () {
  const form = document.getElementById('book-form');
  if (form) {
    form.addEventListener('submit', validateFields);
  }
};

const validateFields = (event) => {
  event.preventDefault();
  const form = document.getElementById('book-form');
  const title = document.getElementById('title');
  const author = document.getElementById('author');

  if (title.value.trim() !== '' && author.value.trim() !== '') {
    form.submit();
  }

  if (title.value.trim() === '') {
    alert('The title cannot be empty.');
    title.focus();
    return false;
  } else if (author.value.trim() === '') {
    alert('The author cannot be empty.');
    author.focus();
    return false;
  }
};

const previewPicture = () => {
  const fileExplorer = document.getElementById('file-explorer');
  fileExplorer.click();

  fileExplorer.addEventListener('change', function () {
    console.log(fileExplorer);
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
  let fileExplorer = document.getElementById('file-explorer');
  const imgPreview = document.getElementById('img-preview');
  imgPreview.src = '';
  fileExplorer.name = 'removeImg';
};
