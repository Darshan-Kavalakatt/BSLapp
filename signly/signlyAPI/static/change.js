
function sign(image, letters){
    
     for (let i = 0; i <letters.length; i++){
        doSetTimeout(i);
        
    }
}
function doSetTimeout(i) {
    setTimeout(function() { image.src = "http://127.0.0.1:8000/api/letters/?letters="+letters[i]}, 500);
  }