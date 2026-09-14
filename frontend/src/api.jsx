const API_URL = "http://localhost:8787";


export async function generate(prompt) {


    const response = await fetch(
        `${API_URL}/api/generate`,
        {

            method: "POST",

            headers: {

                "Content-Type":
                "application/json"

            },


            body: JSON.stringify({

                prompt: prompt

            })

        }
    );


    return await response.json();

}