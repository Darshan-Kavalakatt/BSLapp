
async function checkAnswer(){
    var form = document.getElementById("answer1").querySelector('input:checked').value;
    var form1 = document.getElementById("answer2").querySelector('input:checked').value;
    var form2 = document.getElementById("answer3").querySelector('input:checked').value;
    var form3 = document.getElementById("answer4").querySelector('input:checked').value;
    response = await fetch("http://127.0.0.1:8000/submitclick?a="+form+"&b="+form1+"&c="+form2+"&d="+form3)
    score = await response.text();
    var x = document.createElement("h1");
    var answer = document.createTextNode("Your score is: "+score+"/4");
    x.appendChild(answer);
    var element = document.getElementById("ans");
    element.appendChild(x);
}