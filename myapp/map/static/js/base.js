const time = document.querySelector(".time");
function getCurrentTime() {
    let now = new Date();
    let year = now.getFullYear();
    let month = ("0" + (now.getMonth() + 1)).slice(-2);
    let day = ("0" + now.getDate()).slice(-2);
    let hours = ("0" + now.getHours()).slice(-2);
    let minutes = ("0" + now.getMinutes()).slice(-2);
    
    let formattedTime = year + "년 " + month + "월 " + day + "일 " + hours + "시 " + minutes + "분";
    time.innerHTML = formattedTime;
}

setInterval(getCurrentTime, 1000);  // 1초마다 시간 업데이트