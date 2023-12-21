function deleteNote(noteId) {
  fetch('delete-note', {
    method: 'POST',
    body: JSON.stringify({ noteId: noteId }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((_data) => {
      window.location.href = "/";
    })
    .catch((error) => {
      // Handle any errors that occurred during the fetch
      console.error('There was a problem with the fetch operation:', error);
      // You might want to display an error message to the user here
    });
}