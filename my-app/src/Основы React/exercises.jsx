import { useState } from "react";

const InfoNumber = ({number}) => {
	const digitCount = number.toString().length;
	const isEven = number % 2 === 0;
	const isPerfectSquare = Number.isInteger(Math.sqrt(number));
	
	return (
		<div>
			<h3>Информация о числе {number}:</h3>
			<p>Количество цифр: {digitCount}</p>
			<p>Четное число: {isEven ? 'Да' : 'Нет'}</p>
			<p>Полный квадрат: {isPerfectSquare ? 'Да' : 'Нет'}</p>
		</div>
	);
};

const GetTemp = ({valueK, valueF}) => {

	const handleClickK = (temp) => {
		const tempC = temp - 273.15;
			alert('Температура в Кельвинах: ' + temp + ' =  Температура в Цельсиях: ' + tempC);
	};

	const handleClickF = (temp) => {
		const tempC = (temp - 32) * (5/9);
		alert('Температура в Фаренгейтах: ' + temp + ' =  Температура в Цельсиях: ' + tempC);
	};

	return (
		<div>
			<h2 onClick={() => handleClickK(valueK)}>Температура в Кельвинах: {valueK}</h2>
			<h2 onClick={() => handleClickF(valueF)}>Температура в Фаренгейтах: {valueF}</h2>
		</div>
	);
};

const MyComponent = () => {
	return (
		<div>
			<div align="right" display="flex">
				<hr width="50%" align="right" />
				<h2>Я изучаю React</h2>
			</div>
			<div align="left" display="flex">
				<hr width="50%" align="left" />
				<h2>Я изучаю React</h2>
			</div>
		</div>
	);
};

const CreateRange = ({ firstValue, step }) => {
	const [values, setValues] = useState([Number(firstValue)]);
  
	const handleAdd = () => {
	  setValues(prev => [...prev, prev[prev.length - 1] + Number(step)]);
	};
  
	return (
	  <div>
		{values.join(" ")}{" "}
		<span
		  style={{ cursor: "pointer", fontWeight: "bold" }}
		  onClick={handleAdd}
		>
		  …
		</span>
	  </div>
	);
};


const PowerList = ({ n }) => {
	const items = [];
	for (let i = 1; i <= n; i++) {
	  items.push(
		<li key={i}>
		  {i} <b>**</b> 2 = {i ** 2}
		</li>
	  );
	}
  
	return <ul>{items}</ul>;
};

export {InfoNumber, GetTemp, MyComponent, CreateRange, PowerList};
