module.exports = {
    plugins: [
        require("@tailwindcss/typography"),
        require("daisyui")
    ],
    daisyui: {
        themes: ["cupcake", "dark"]
    },
    content: [
        "./server/templates/**/*.{html,xhtml}",
        "./server/static/styles/src/*.css"
    ]
}