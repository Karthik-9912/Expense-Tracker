let btn=document.querySelector("#transactionBtn");
let div=document.querySelector(".spent-sec")

btn.addEventListener("click",(event)=>{
    event.stopPropagation();
    div.classList.toggle("visible")
    
});

// 
window.addEventListener("click",(event)=>{
    if(!div.contains(event.target) && !btn.contains(event.target)){
        div.classList.remove("visible")
    }
});