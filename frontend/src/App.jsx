import { useState } from "react";

import { generate } from "./api";


function App() {


    const [prompt, setPrompt] = useState("");

    const [result, setResult] = useState("");



    async function handleGenerate() {


        const data = await generate(prompt);


        setResult(
            JSON.stringify(
                data,
                null,
                2
            )
        );

    }



    return (

        <div style={{padding:"40px"}}>


            <h1>
                AI KiCad Copilot
            </h1>


            <textarea

                rows="6"

                cols="50"

                placeholder="Example: Create a PCB project"

                value={prompt}

                onChange={
                    e => setPrompt(e.target.value)
                }

            />


            <br/>


            <button
                onClick={handleGenerate}
            >

                Generate KiCad Project

            </button>



            <h3>
                Result
            </h3>


            <pre>

                {result}

            </pre>


        </div>

    );

}


export default App;