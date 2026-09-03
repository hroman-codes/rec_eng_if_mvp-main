// Progressive enhancement only: authentication, tags and editing work without JS.
document.querySelectorAll('[data-password]').forEach(button => {
  button.addEventListener('click', () => {
    const input = document.getElementById(button.dataset.password);
    const showing = input.type === 'password';
    input.type = showing ? 'text' : 'password';
    button.setAttribute('aria-pressed', String(showing));
    button.setAttribute('aria-label', `${showing ? 'Hide' : 'Show'} password`);
    button.querySelector('i').className = showing ? 'bi bi-eye-slash' : 'bi bi-eye';
  });
});
document.querySelectorAll('[data-dismiss]').forEach(button => {
  button.addEventListener('click', () => button.closest('.notice').remove());
});
document.querySelectorAll('.field-errors').forEach(errors => {
  const input = errors.closest('.field').querySelector('input, textarea');
  if (input) {
    input.setAttribute('aria-invalid', 'true');
    input.setAttribute('aria-describedby', errors.id);
  }
});
const editor = document.getElementById('edit-contact');
if (editor) {
  editor.scrollIntoView({ block: 'start' });
  editor.querySelector('[aria-invalid="true"], input:not([type="hidden"])')?.focus({ preventScroll: true });
}
