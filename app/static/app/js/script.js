let wallet=document.querySelector(".wallet-info")
let overview=document.querySelector(".overview")

wallet.addEventListener("click",(e)=>{
    window.location.href=transactionUrl;
});

let profileClick = document.querySelector("#profile")

profileClick.addEventListener("click",()=>{
    document.querySelector(".logout-btn").classList.toggle("show");
    
})

