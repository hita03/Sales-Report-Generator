
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const alertBox = document.getElementById('alert-box')
console.log(alertBox)
const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}
console.log("hi")
Dropzone.autoDiscover = false
console.log(document.getElementById("my-dropzone"))
const myDropzone = new Dropzone("#my-dropzone", {
    url:'/reports/',//'http://127.0.0.1:8000/reports/',
    init: function() {
        this.on('sending', function(file, xhr, formData){
            console.log("sending")
            formData.append('csrfmiddlewaretoken', csrf)
        })
        this.on('success', function(file, response){
            //console.log(response.ex)
            if(response.ex) {
                handleAlerts('danger', 'This file already exists, it was uploaded before.')
            } else {
                handleAlerts('success', 'Your file has been uploaded!')
            }
        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.csv'
})



/*

    Dropzone.autoDiscover = false
    const dropzone_element = document.getElementsByClassName('dropzone dstyle')
    console.log(document.getElementById("my_dropzone")) 
    const myDropzone = new Dropzone("#my_dropzone",{
        
        url: '/reports/upload/',
        init: function(){
            this.on('sending', function(file, xhr,formData){
                console.log(csrf)
                console.log("sending")
                formData.append('csrfmiddlewaretoke',csrf)
            })
        },
        maxFiles: 3,
        maxFilesize: 3,
        acceptedFiles: '.csv'
        
    })
    console.log("hi")
    */