function ImagePopup(imageUrl) {
    // 팝업 엘리먼트 생성
    const check_popup = document.querySelector(".img-popup");
    if(check_popup){
        return 0;
    }
    const popup = document.createElement("div");
    popup.className = "img-popup";
    
    // 이미지 엘리먼트 생성
    const image = document.createElement("img");
    image.src = imageUrl;
    image.style.maxWidth = "100%";
    image.style.maxHeight = "100%";
    
    // 이미지를 팝업에 추가
    popup.appendChild(image);
    
    // 닫기 버튼 생성
    const closeButton = document.createElement("span");
    closeButton.innerHTML = "X";
    closeButton.className = "close-button";

    // 닫기 버튼 클릭 이벤트 처리
    closeButton.addEventListener("click", function () {
        popup.style.display = "none";
        document.body.removeChild(popup);
    });
    // 팝업에 닫기 버튼 추가
    popup.appendChild(closeButton);

    // 팝업을 body에 추가
    document.body.appendChild(popup);
    
    // 팝업을 보여줌
    popup.style.display = "block";
    
}

