async function test(){
    // alert("hello");
    const url="http://127.0.0.1:8000/ph/api/menu/";
    let menuInfo = document.getElementById('data');
            menuInfo.innerHTML ='';
    try{
        
        const response = await fetch(url,{
            method: "GET",
            mode: "cors",
        }

        );
        console.log('checking response');
        if(!response.ok){
            throw new Error (`Response Status: ${response.status}`)
        }
        const json_data=await response.json();
        console.log(json_data);
        
        for (i of json_data){
            console.log(i.title);
            menuInfo.innerHTML += `<p>${i.title}</p>`
        }
    }catch(error){
        console.error('error info: '+error.message);
        menuInfo.innerHTML = '<p style="color:red;">The server is down. Please try again later.</p>';
    }
}
window.onload=test;