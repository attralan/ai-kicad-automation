import {useState} from "react";

import {generate, downloadUrl} from "./api";

function App(){

  const [prompt,setPrompt]=useState("");

  const [result,setResult]=useState("");

  const [files,setFiles]=useState([]);

  const [projectName,setProjectName]=useState("");

  async function run(){

    const data =
      await generate(prompt);

    setResult(

      JSON.stringify(

        data,

        null,

        2

      )

    );

    setFiles(data.files || []);

    setProjectName(data.project_name || "");

  }

  return (

    <div>

      <h1>
        AI KiCad Copilot
      </h1>

      <textarea

        value={prompt}

        onChange={

          e=>setPrompt(e.target.value)

        }

      />

      <button

        onClick={run}

      >

        Generate KiCad Project

      </button>

      {files.length > 0 && (

        <div>

          <h3>Generated Files</h3>

          <ul>

            {files.map((f) => (

              <li key={f}>

                {f}{" "}

                <a href={downloadUrl(projectName, f)} download>

                  Download

                </a>

              </li>

            ))}

          </ul>

        </div>

      )}

      <pre>

        {result}

      </pre>

    </div>

  )

}

export default App;
