let wallet=document.querySelector(".wallet-info")
let overview=document.querySelector(".overview")

wallet.addEventListener("click",(e)=>{
    window.location.href=transactionUrl;
});

let profileClick = document.querySelector("#profile")

profileClick.addEventListener("click",()=>{
    document.querySelector(".logout-btn").classList.toggle("show");
    
})

let addNewBtn = document.querySelector('.new-wallet');
let premiumFeature = document.querySelector(".premium-container");

addNewBtn.addEventListener("click",(e)=>{
    e.stopPropagation();
    premiumFeature.style.display="block";
})

let removeFeature = document.getElementById("rm-btn");

removeFeature.addEventListener("click",(e)=>{
    e.stopPropagation();
    premiumFeature.style.display="none";
})

