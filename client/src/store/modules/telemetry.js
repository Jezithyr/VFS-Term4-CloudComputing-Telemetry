
/*
    Copyright (C) Sabastian Peters 2020
*/


import Datastore from "@/lib/Datastore.js";



// ## STATE ##
const state = {
    isFetchingData: false,
    entityList: [],
    entityFormat: {
        date: { displayName: "Date" },
        sessionId: { displayName: "Session Id" },
        user: { displayName: "User" },
        y: { displayName: "Position X" },
        x: { displayName: "Position Y" },
        value: { displayName: "Value" },
    }
}


// ## GETTERS ##
const getters = {}



// ## ACTIONS ##
const actions = {
    fetchEntityList: async (context) => {

        context.commit("SET_IS_FETCHING_DATA", true);

        // gets the entity list and stores it in vue variable
        let response = await Datastore.get();

        context.commit("SET_ENTITY_LIST", response.data.entityList);
        context.commit("SET_IS_FETCHING_DATA", false);

    }
}


// ## MUTATIONS ##
const mutations = {
    SET_IS_FETCHING_DATA: (state, value) => {
        state.isFetchingData = value;
    },
    SET_ENTITY_LIST: (state, value) => {
        state.entityList = value;
    },
}





export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}