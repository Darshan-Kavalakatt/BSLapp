
async function checkAnswer(result){
    var form = document.getElementById("answer1").querySelector('input:checked').value;
    var form1 = document.getElementById("answer2").querySelector('input:checked').value;
    console.log(document.getElementById("answer1").querySelector('input:checked').value)
    console.log(document.getElementById("answer2").querySelector('input:checked').value)
    response = await fetch("http://127.0.0.1:8000/submitclick?a="+form+"&b="+form1)
    text = await response.text()
    console.log(response)  
    console.log(text)
    result.innerHTML = "you got "+text+" out of 2"
}