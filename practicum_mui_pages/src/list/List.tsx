import Navbar from "../components/Navbar";
import BuildingsGrid from "./components/BuildingsGrid";

function List() {
  return (
    <div>
      <Navbar activePage="2" />
      <BuildingsGrid/>
    </div>
  );
}
export default List;
