const loader = document.querySelector(".loader");

let pageNo = 2;
let isScrollEventEnabled = true;

function loadMoreContent(callback) {
    // AJAX 요청 보내기
    const url = "tour_data/loaderFestivalList?pageNo="+encodeURIComponent(pageNo)
    fetch(url)
    .then(response => response.json())
    .then(data => {
    // 응답 처리
    if (data.content) {
        // 응답 데이터를 HTML 형식으로 변환하여 loader에 추가
        let contentHTML = "";
        for (let item of data.content.item) {
            contentHTML += '<div class="col mb-5">';
            contentHTML += '<div class="card h-100">';
            contentHTML += '<img class="img-thumbnail card-img-height" src="' + item.firstimage + '" alt="..." />';
            contentHTML += '<div class="card-body p-4">';
            contentHTML += '<div class="text-center">';
            contentHTML += '<h5 class="fw-bolder">' + item.title + '</h5>';
            contentHTML += '<div class="date">' + item.eventstartdate.slice(0, 4) + '.' + item.eventstartdate.slice(4, 6) + '.' + item.eventstartdate.slice(6, 8) + ' ~ ' + item.eventenddate.slice(0, 4) + '.' + item.eventenddate.slice(4, 6) + '.' + item.eventenddate.slice(6, 8) + '</div>';
            contentHTML += '</div>';
            contentHTML += '</div>';
            contentHTML += '</div>';
            contentHTML += '</div>';
        }
        loader.innerHTML += contentHTML;
        pageNo++;
        if (typeof callback === 'function') {
            callback();
        }
    } else {
        loader.innerHTML += "더 이상 콘텐츠가 없습니다.";
    }
    })
    .catch(error => {
    console.error(error);
    });
}

function handleScroll() {
    if (!isScrollEventEnabled) {
        return;
    }

    const scrollHeight = document.documentElement.scrollHeight;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const clientHeight = window.innerHeight || document.documentElement.clientHeight;

    if (scrollHeight - scrollTop <= clientHeight + 200) {
        isScrollEventEnabled = false; // 스크롤 이벤트 비활성화

        loadMoreContent(function() {
            isScrollEventEnabled = true; // loadMoreContent 함수 실행이 완료된 후 스크롤 이벤트 다시 활성화
        });
    }
}

window.addEventListener("scroll", handleScroll);

