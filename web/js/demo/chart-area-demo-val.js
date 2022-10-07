import {todayCount, selectTest, dayTotal, dayPerson, personCount} from "../db/firebase-connect.js";
// selectTest()
let count = await todayCount();
console.log("count out : "+count);

// dayPerson();

personCount();