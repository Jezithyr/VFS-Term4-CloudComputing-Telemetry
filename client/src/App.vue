<template>
    <div id="app-wrapper">
        <div id="app-container">
            <div id="nav">
                <router-link to="/">View</router-link> |
                <router-link to="/admin/upload">Upload</router-link>
            </div>
            <router-view />
        </div>
    </div>
</template>





<style>

#app-wrapper {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;

    display: flex;
    flex-flow: column nowrap;
    align-items: center;
}

#app-container {
    width: 100%;
    min-width: 200px;
    max-width: 800px;

    display: flex;
    flex-flow: column nowrap;
    align-items: center;

    text-align: center;
}




/* ## NAVIGATION BAR ## */

#nav {
    padding: 30px;
}
#nav a {
    font-weight: bold;
    color: #2c3e50;
}
#nav a.router-link-exact-active {
    color: #42b983;
}
</style>
