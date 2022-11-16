let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', (e) => {
            e.preventDefault()
            let page = e.target.dataset.page
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
            searchForm.submit()
        })
    }
}