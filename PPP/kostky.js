function hod_kostkou(typKostky) {
    num = Math.floor(Math.random() * typKostky) + 1;
    document.getElementById('kostka').textContent = num;
}