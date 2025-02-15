// let search = document.getElementsByClassName('search-input')[0];
// let searchButton = document.getElementsByClassName('search-btn')[0];

// searchButton.addEventListener('click', () => {
//     let movie = search.value;
//     movieID(movie);
// });

// search.addEventListener('keypress', (e) => {
//     if (e.key === 'Enter') {
//         e.preventDefault();
//         let movie = search.value;
//         movieID(movie);
//     }
// });

// async function movieID(movie){
//     const url = `http://www.omdbapi.com/?t=${movie}&apikey=13510fc9`;
//     try{
//         const response = await fetch(url);
//         const result = await response.json();
//         console.log(result);
//         if (result.Response === "True") {
//             fetchData(result.imdbID);
//         } else {
//             console.error("Movie not found");
//         }
//     } catch(error){
//         console.error(error);
//     }
// }


// async function fetchData(imdbID) {

//     const url = `https://imdb236.p.rapidapi.com/imdb/${imdbID}`;
//     const options = {
//         method: 'GET',
//         headers: {
//             'x-rapidapi-key': '51ebc20289msh70b6fe9f5555adfp196b93jsn22fa3f5c185e',
//             'x-rapidapi-host': 'imdb236.p.rapidapi.com'
//         }
//     };
    
//     try {
//         const response = await fetch(url, options);
//         const result = await response.json();
//         console.log(result);
//     } catch (error) {
//         console.error(error);
//     }
// }

// async function sendMovieDataToBackend(movieData) {
//     const url = '/https://imdb236.p.rapidapi.com/imdb/save_movie';
//     try {
//         const response = await fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(movieData)
//         });
//         const result = await response.json();
//         console.log(result);
//     } catch (error) {
//         console.error(error);
//     }
// }


let search = document.getElementsByClassName('search-input')[0];
let searchButton = document.getElementsByClassName('search-btn')[0];

searchButton.addEventListener('click', () => {
    let movie = search.value;
    movieID(movie);
});

search.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        let movie = search.value;
        movieID(movie);
    }
});

async function movieID(movie){
    const url = `http://www.omdbapi.com/?t=${movie}&apikey=13510fc9`;
    try{
        const response = await fetch(url);
        const result = await response.json();
        console.log(result);
        if (result.Response === "True") {
            fetchData(result.imdbID);
            sendMovieDataToBackend(result);
        } else {
            console.error("Movie not found");
        }
    } catch(error){
        console.error(error);
    }
}


async function fetchData(imdbID) {

    const url = `https://imdb236.p.rapidapi.com/imdb/${imdbID}`;
    const options = {
        method: 'GET',
        headers: {
            'x-rapidapi-key': '51ebc20289msh70b6fe9f5555adfp196b93jsn22fa3f5c185e',
            'x-rapidapi-host': 'imdb236.p.rapidapi.com'
        }
    };
    
    try {
        const response = await fetch(url, options);
        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
}
async function sendMovieDataToBackend(imdbID) {
    const url = '/https://imdb236.p.rapidapi.com/imdb/save_movie';
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(imdbID)
        });
        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
}