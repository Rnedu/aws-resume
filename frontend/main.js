window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
})

const functionApi = 'https://osn3nqzakpwdxbb3nlfc2nal3y0pgmwa.lambda-url.ap-southeast-2.on.aws/';

const getVisitCount = () => {
    fetch(functionApi)
        .then(response => response.json())
        .then(response => {
            console.log("Website called function API.");
            const count = response.updatedCount;  // Use 'updatedCount' instead of 'count'
            document.getElementById("counter").innerText = count;
        })
        .catch(function(error) {
            console.log(error);
        });
}
