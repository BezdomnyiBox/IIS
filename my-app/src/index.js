import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import {InfoNumber, GetTemp, MyComponent, CreateRange, PowerList} from "./Основы React/exercises";

const root = ReactDOM.createRoot(document.getElementById("root"));


const element = (
	<div>
		<MyComponent/>
		<InfoNumber number={332321}/>
		<GetTemp valueK={300} valueF={100}/>
		<CreateRange firstValue={1} step={2}/>
		<PowerList n={10}/>
	</div>
);




root.render(element);
