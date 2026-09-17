export async function generate(prompt){

  const response = await fetch(

    "http://127.0.0.1:8787/api/generate",

    {

      method:"POST",

      headers:{

        "Content-Type":

        "application/json"

      },

      body:JSON.stringify({

        prompt:prompt

      })

    }

  );

  return response.json();

}

export function downloadUrl(projectName, filename){

  return `http://127.0.0.1:8787/api/download/${projectName}/${filename}`;

}
