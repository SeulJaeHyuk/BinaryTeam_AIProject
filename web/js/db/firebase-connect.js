import { initializeApp } from 'firebase/app';
import { getDatabase, ref, child, get, onValue  } from 'firebase/database';
// import { initializeApp } from  '/node_modules/firebase/app/dist/index.cjs.js';
// import { getDatabase} from '/node_modules/firebase/database/dist/public.d.ts';
// import { getDatabase, ref,get, set, child, update, remove } from '/node_modules/firebase/database/dist/public.d.ts';
// node_modules/firebase/database/dist/public.d.ts
// node_modules\@firebase\database\dist\public.d.ts
// node_modules\@firebase\database\dist\public.d.ts
// 




const firebaseConfig = {
    apiKey: "AIzaSyBETK45cbP1g2ZYC03ras5UYys5fXAqV_4",
    authDomain: "fir-course-edb8c.firebaseapp.com",
    databaseURL: "https://fir-course-edb8c-default-rtdb.firebaseio.com",
    projectId: "fir-course-edb8c",
    storageBucket: "fir-course-edb8c.appspot.com",
    messagingSenderId: "760960563313",
    appId: "1:760960563313:web:eb3b145202888f8a3c83d0",
    measurementId: "G-336MJ5MK72"
  };

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);


const selectTest = function(){
    const dbref = ref(db);

    get(child(dbref,"test")).then((snapshot)=>{
        if(snapshot.exists()){
            let arr = [];
            snapshot.forEach(childSnapshot=>{
                console.log(childSnapshot.val());
                arr.push(childSnapshot.val());
            })
            console.log(arr);
        }
        else{
            console.log("not data");
        }
    })
    .catch((error)=>{
        console.log("error : "+error);
    });
}
// const dayCount = async function(){
//     const dbref = ref(db);
//     let count = 0;

//     let today = new Date();
//     let year = today.getFullYear();
//     let month = today.getMonth() + 1; 
//     month = month <10 ? '0'+month:month;
//     let date = today.getDate();
//     date = 26;
//     await get(child(dbref,"club/"+year+"/"+month+"/"+date)).then( function(snapshot){
//         if(snapshot.exists()){
//             snapshot.forEach(childSnapshot => {
//                 console.log(childSnapshot.val());
//                 count++;
//             });
//         }
//     });
//     return count;
//   }

const todayCount = async function(){
    const dbref = ref(db);
    let count = 0;

    let today = new Date();
    let year = today.getFullYear();
    let month = today.getMonth() + 1; 
    month = month <10 ? '0'+month:month;
    let date = today.getDate();
    date = 26;
    let snapshot = await get(child(dbref,"club/"+year+"/"+month+"/"+date))
    if (snapshot.exists) {
        snapshot.forEach(childSnapshot => {
            count++;
        });
    }
    return count;
  }
const dayTotal = async function(){
    const dbref = ref(db);
    let returns = {};
    let count =0;
    let today = new Date();
    let year = today.getFullYear();
    let month = today.getMonth() + 1; 
    month = month <10 ? '0'+month:month;

    let snapshot = await get(child(dbref,"club/"+year+"/"+month));
    if(snapshot.exists){
        console.log(snapshot.key);
        snapshot.forEach(childSnapshot=>{
            console.log(childSnapshot.key);
            childSnapshot.forEach(item =>{
                count++;
            })
            returns[childSnapshot.key] = count;
            count = 0;
        })
    }
    console.log(returns);
    return returns;
}
const dayPerson = async function(){
    const dbref = ref(db);
    let returns = {};
    let list = {};
    let count =0;
    let today = new Date();
    let year = today.getFullYear();
    let month = today.getMonth() + 1; 
    month = month <10 ? '0'+month:month;

    let snapshot = await get(child(dbref,"club/"+year+"/"+month));
    if(snapshot.exists){
        snapshot.forEach(childSnapshot=>{
            childSnapshot.forEach(item =>{
                let dic = item.val();
                let keyList = Object.keys(dic);
                let name = keyList[0];
                if('Unknown' == name){}
                else if(name in list){
                    list[name] = list[name] + 1;
                }
                else{
                    list[name] = 1;
                }
            })
            returns[childSnapshot.key] = list;
            list = {};
        })
    }
    console.log(returns);
    return returns;
}

const personCount = async function(){
    const dbref = ref(db);
    let count = 0;

    let snapshot = await get(child(dbref,"person"));
    if(snapshot.exists){
        snapshot.forEach(key=>{
            count++;
        })
    }
    return count;
}





// const select = function(){
//     console.log("select");
// }
export {selectTest , todayCount, dayTotal, dayPerson, personCount};