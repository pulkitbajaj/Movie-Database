document.addEventListener("DOMContentLoaded", function () {


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

    async function movieID(movie) {
        const url = `http://www.omdbapi.com/?t=${movie}&apikey=13510fc9`;
        try {
            const response = await fetch(url);
            const result = await response.json();
            console.log(result);
            if (result.Response === "True") {
                fetchData(result.imdbID);
                sendMovieDataToBackend(result);
            } else {
                console.error("Movie not found");
            }
        } catch (error) {
            console.error(error);
        }
    }


    async function fetchData(imdbID) {

        const url = `https://imdb236.p.rapidapi.com/imdb/${imdbID}`;
        const options = {
            method: 'GET',
            headers: {
                'x-rapidapi-key': 'f7fa5f4e6bmsh11ab2dcaf3eb9bbp1be04bjsn67365ee606c9',
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


    async function banner(imdbID) {
        const url = `https://imdb236.p.rapidapi.com/imdb/${imdbID}`;
        const options = {
            method: 'GET',
            headers: {
                'x-rapidapi-key': 'f7fa5f4e6bmsh11ab2dcaf3eb9bbp1be04bjsn67365ee606c9',
                'x-rapidapi-host': 'imdb236.p.rapidapi.com'
            }
        };

        try {

            const response = await fetch(url, options);
            const result = await response.json();
            console.log(result);

            let title = document.getElementById("Movie_Title");
            title.innerHTML = result.primaryTitle;

            let bannerDescription = document.getElementById("mv-desc")
            if (result && result.description) {
                bannerDescription.innerHTML = result.description;
            } else {
                console.error("Banner description not found");
            }
            let bannerImage = document.getElementById("banner-image");

            // Ensure the element exists and result contains valid data
            if (bannerImage && result && result.primaryImage) {
                bannerImage.src = result.primaryImage;  // Use correct property access
                // bannerImage.alt = result.titleText.text;
            } else {
                console.error("Banner image not found or result is invalid");
            }

            console.log("API Response:", result);

        // Call function to update background
        updateBackground(result);
    } catch (error) {
        console.error("❌ Error fetching API:", error);
    }
}

function updateBackground(result) {
    try {
        let backgroundImg = document.getElementsByClassName("banner")[0];

        if (!backgroundImg) {
            throw new Error("❌ Element with class 'banner' not found");
        }

        // Use the correct field from API response
        const imageUrl = result.primaryImage; // Correct field!

        if (imageUrl) {
            backgroundImg.style.backgroundImage = `url('${imageUrl}')`;
            backgroundImg.style.backgroundSize = "contain";
            backgroundImg.style.backgroundPosition = "center";
            console.log("✅ Background updated with:", imageUrl);
        } else {
            console.warn("⚠️ Image URL is missing in the API response.");
        }

    } catch (error) {
        console.error("❌ Error:", error);
    }
    }

    banner('tt1375666');



    const topMovies = 'https://imdb236.p.rapidapi.com/imdb/most-popular-movies';
const options = {
	method: 'GET',
	headers: {
		'x-rapidapi-key': 'f7fa5f4e6bmsh11ab2dcaf3eb9bbp1be04bjsn67365ee606c9',
		'x-rapidapi-host': 'imdb236.p.rapidapi.com'
	}
};
    async function top10Movies() {
        try {
            const response = await fetch(topMovies, options);
            const result = await response.json();
            // console.log(result);
            for (let i = 0; i < 5; i++) {
                let mv = document.getElementById((i + 1).toString());
                if (result && result.length > i) {
                    mv.src = result[i].primaryImage;
                } else {
                    console.error(`Movie ${i + 1} not found`);
                }
            }
        } catch (error) {
            console.error(error);
        }
    }

    top10Movies();

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


});