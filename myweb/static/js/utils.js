

function SavePageCount() {
    if (localStorage.Pagecount) {
        localStorage.Pagecount = Number(localStorage.Pagecount) + 1;
    }else{
        localStorage.Pagecount = 1;
    }
    //document.write("visit" + localStorage.pagecount + "times");
    document.getElementById("pagecount").innerText = "pagecount:" + localStorage.Pagecount;
    //$("pagecount").(localStorage.Pagecount);
}