document.addEventListener("DOMContentLoaded", function() {
    // ボタン要素を作成
    let button = document.createElement("button");
    button.innerText = "背景を変える";
    document.body.appendChild(button);

    // ボタンがクリックされたときに背景色を変える
    button.addEventListener("click", function() {
        document.body.style.backgroundColor = 
            document.body.style.backgroundColor === "lightblue" ? "white" : "lightblue";
    });
});

document.addEventListener("DOMContentLoaded", function() {
    let rows = document.querySelectorAll("tbody tr");
    rows.forEach(row => {
        row.addEventListener("click", function() {
            this.style.display = "none"; // 行を非表示にする
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    let table = document.querySelector("table");  
    table.style.opacity = 0;  // 最初は透明

    let fadeEffect = setInterval(function() {
        if (table.style.opacity < 1) {
            table.style.opacity = parseFloat(table.style.opacity) + 0.05; // だんだん表示
        } else {
            clearInterval(fadeEffect);
        }
    }, 50); // 50msごとに少しずつ表示
});
