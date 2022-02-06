const hiddens = document.getElementsByClassName("trainingcard");
hiddens[0].classList.remove('is-hidden');

var start = 0 // as hiddens[0] is unhidden already
function getNext(element) {
    if (start < hiddens.length) {
        console.log(start, hiddens.length);
        hiddens[start].classList.add('is-hidden');
        if (h = hiddens[start + 1]) {
            h.classList.remove('is-hidden');
        } else {
            element.classList.add('is-hidden');
            document.getElementById('quizbutton').classList.remove('is-hidden');
        }
        start++;
    }
}