window.onload = function () {
  const dropdown = document.getElementById('order-dropdown');
  if (dropdown) {
    dropdown.value = '';
  }
};

const validateFields = (event) => {
  event.preventDefault();
  const form = document.getElementById('book-form');
  const title = document.getElementById('title');
  const author = document.getElementById('author');

  if (title.value.trim() !== '' && author.value.trim() !== '') {
    showLoader(true);
    form.submit();
  }

  if (title.value.trim() === '') {
    alert('The title cannot be empty.');
    title.focus();
  } else if (author.value.trim() === '') {
    alert('The author cannot be empty.');
    author.focus();
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
  const fileExplorer = document.getElementById('file-explorer');
  const imgPreview = document.getElementById('img-preview');
  imgPreview.src = '/static/assets/book-stock.png';
  fileExplorer.name = 'removeImg';
};

const showConfirmation = (event) => {
  if (!confirm('Are you sure you want to delete this book?')) {
    event.preventDefault();
  } else {
    showLoader(true);
  }
};

const orderBooks = () => {
  showLoader(true);
  const dropdown = document.getElementById('order-dropdown');
  if (dropdown.value !== '') {
    const books = document.getElementById('books');

    fetch(`/?order_by=${dropdown.value}`)
      .then((response) => response.json())
      .then((data) => {
        showLoader(false);
        books.innerHTML = data.data;
      })
      .catch((error) => {
        showLoader(false);
        console.error('Error:', error);
      });
  }
};

const showLoader = (show) => {
  const loader = document.getElementById('loader-container');
  if (show) {
    loader.style.display = 'flex';
  } else {
    loader.style.display = 'none';
  }
};
