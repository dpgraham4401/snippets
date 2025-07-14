import './index.css'
import {Login} from "./components/Login.tsx";

function App() {

    return (
        <div className="h-screen w-screen bg-slate-100">
            <header className="bg-slate-700 p-5 mb-5">
                <h1 className="text-gray-200">HELLO</h1>

            </header>
            <div className="flex justify-center items-center align-middle min-h-[calc(100vh-80px)]">
                <div>
                    <Login/>
                </div>
            </div>
        </div>
    )
}

export default App
