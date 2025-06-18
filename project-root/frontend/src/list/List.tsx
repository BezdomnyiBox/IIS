import Navbar from "../components/Navbar";
import CountriesGrid from "./components/CountriesGrid";
import Footer from "../components/Footer";

function List() {
  return (
    <div>
      <Navbar activePage="2" />
      <CountriesGrid/>
      <Footer/>
    </div>
  );
}
export default List;
