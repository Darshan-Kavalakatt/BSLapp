async function sign(image, letters) {
    for (let i = 0; i < letters.length; i++) {
        await sleep(500);
        image.src = "http://127.0.0.1:8000/api/letters/?letters=" + letters[i]
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function checkAPI(word){
    response = await fetch("http://127.0.0.1:8000/api/videolink?word="+word)
    if(response.status == 200) {
        text = await response.text()
        return text;
    } else {
        return false;
    }
}

async function wordsplitter(image,video,letters){
    url = await checkAPI(letters);
    if(url) {
        video.src = url
        video.style.display = "block"; 
        return;
    }
    
    var words = letters.split(" ");
    for(let i = 0; i< words.length; i++){
        if(await checkAPI(words[i])==false){
            for(let y = 0;y<words[i].length;y++){
                image.src = "http://127.0.0.1:8000/api/letters/?letters=" + words[i][y]
                image.style.display = "block"; 
                await sleep(750);
                image.style.display = "none";
            }
        }else{
            video.style.display = "block"; 
            video.src = await checkAPI(words[i]);
            await sleep(4000);
            video.style.display = "none"; 
        }
    }
    
    


}