let btnDownload1 = document.querySelector('#img1_download');
let img = document.querySelector('#d_preview1_img');
// Must use FileSaver.js 2.0.2 because 2.0.3 has issues.
btnDownload1.addEventListener('click', () => {
    let imagePath = img.getAttribute('src');
    let fileName = getFileName(imagePath);
    saveAs(imagePath, fileName);
});
function getFileName(str) {
    return str.substring(str.lastIndexOf('/') + 1)
}


// img 2 
let btnDownload2 = document.querySelector('#img2_download');
let img2 = document.querySelector('#d_preview2_img');
// Must use FileSaver.js 2.0.2 because 2.0.3 has issues.
btnDownload2.addEventListener('click', () => {
    let imagePath = img2.getAttribute('src');
    let fileName = getFileName(imagePath);
    saveAs(imagePath, fileName);
});
function getFileName(str) {
    return str.substring(str.lastIndexOf('/') + 1)
}

// image 3 
let btnDownload3 = document.querySelector('#img3_download');
let img3 = document.querySelector('#d_preview3_img');
// Must use FileSaver.js 2.0.2 because 2.0.3 has issues.
btnDownload3.addEventListener('click', () => {
    let imagePath = img3.getAttribute('src');
    let fileName = getFileName(imagePath);
    saveAs(imagePath, fileName);
});
function getFileName(str) {
    return str.substring(str.lastIndexOf('/') + 1)
}

// image 4 
let btnDownload4 = document.querySelector('#img4_download');
let img4 = document.querySelector('#d_preview4_img');
// Must use FileSaver.js 2.0.2 because 2.0.3 has issues.
btnDownload4.addEventListener('click', () => {
    let imagePath = img4.getAttribute('src');
    let fileName = getFileName(imagePath);
    saveAs(imagePath, fileName);
});
function getFileName(str) {
    return str.substring(str.lastIndexOf('/') + 1)
}