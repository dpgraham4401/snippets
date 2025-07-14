/**
 * A simple login component using controlled form elements
 */
import {type FormEvent, useState} from "react";

const passwordRequirements = {
    length: {
        check: (val: string) => val.length > 12,
        error: "Password must by 12 character's long"
    },
    capitalLetter: {
        check: (val: string) => /[A-Z]/.test(val),
        error: "Password must contains a capital letter"
    }
}

export const Login = () => {
    const [email, setEmail] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [confirmPassword, setConfirmPassword] = useState<string>('');
    const [error, setError] = useState<string>('');

    const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setError('')
        for (const key in passwordRequirements) {
            if (!passwordRequirements[key].check(password)) {
                console.log("check did not pass")
                setError(passwordRequirements[key].error)
            }
        }
        if (password !== confirmPassword) {
            setError("Passwords do not match")
        }
        console.log({email, password, confirmPassword})
    }

    return (
        <div className="bg-white rounded-2xl shadow-lg p-8 max-h-1/4 min-h-56">
            <h2 className="font-bold text-slate-700">Login</h2>
            <form className="mx-auto max-w-sm" onSubmit={handleSubmit}>
                <div className="my-1">
                    <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your
                        email</label>
                    <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" id="email"
                           className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                           placeholder="bob@gmail.com" required/>
                </div>
                <div className="my-1">
                    <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Password
                    </label>
                    <input onChange={(e) => setPassword(e.target.value)} value={password} type="password" id="password"
                           className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                           placeholder="password" required/>
                </div>
                <div className="my-1">
                    <label htmlFor="confirmPassword"
                           className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Confirm Password
                    </label>
                    <input onChange={(e) => setConfirmPassword(e.target.value)} value={confirmPassword} type="password"
                           id="confirmPassword"
                           className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                           placeholder="confirm password" required/>
                </div>
                <button type="submit" className="bg-cyan-800 text-white rounded-lg p-2 my-2">
                    Login
                </button>
            </form>
            {error && (
                <div className="flex items-center bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded mt-2">
                    <p className="text-sm">{error}</p>
                </div>
            )}
        </div>
    )
}