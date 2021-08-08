console.log("hello world")

const reportbtn = document.getElementById('report-btn')
const img = document.getElementById('img')
const modalBody = document.getElementById('modal-body')
const reportForm = document.getElementById('report-form')
const alertbox = document.getElementById('alert-box')

const reportName = document.getElementById('id_name')
const reportRemarks = document.getElementById('id_remarks')
const csrf =document.getElementsByName('csrfmiddlewaretoken')[0].value


console.log("hi")
if(img)
{
   reportbtn.classList.remove("not-visible")
}
console.log(img)

reportbtn.addEventListener('click', ()=>{
    console.log('clicked')
    img.setAttribute('class','w-100')
    console.log(modalBody.append(img))
    modalBody.prepend(img)


    reportForm.addEventListener('submit', e=>{
        e.preventDefault()
        const formdata = new FormData()
        formdata.append('csrfmiddlewaretoken',csrf)
        formdata.append('name',reportName.value)
        formdata.append('remarks',reportRemarks.value)
        formdata.append('image',img.src)


        $.ajax({
            type: 'POST',
            url: '/reports/save/',
            data: formdata,
            success: function(response){
                console.log(response)
                handleAlert('success','Report Saved!')
            },
            error: function(error){
                console.log(error)
                handleAlert('danger','Report not saved. Something went wrong.')
            },
            processData: false,
            contentType: false,
        })
    })
})

const handleAlert = (type, message) =>{
    alertbox.innerHTML =`<div class="alert alert-${type}" role="alert">
    ${message}
    </div>`
}