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
