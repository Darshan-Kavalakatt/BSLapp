async function sign(image, letters) {
    for (let i = 0; i < letters.length; i++) {
        await sleep(500);
        image.src = "http://127.0.0.1:8000/api/letters/?letters=" + letters[i]
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}