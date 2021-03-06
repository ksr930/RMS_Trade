import React from "react";
import { connect } from "react-redux";
import { loadNetPositionsDataSocket, netpositonsData } from "../../actions";
// import io from "socket.io-client";
import { Link } from "react-router-dom";

import { Menu, Sticky, Breadcrumb } from "semantic-ui-react";

let columns = ["Client ID", "Symbol", "Net Quantity"];
// let socket;
// let buy_sell_flag;
let quantity_flag;

class NCP extends React.Component {
  render() {
    // console.log(this.props)
    return (
      <div>
        <Sticky>
          <Menu style={{ margin: 0 }}>
            <a href="/clientnetposition">
              <Menu.Item>Client Net Positions</Menu.Item>
            </a>
            <Link to="/clientnetposition/d18138">
              <Menu.Item>D18138</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d7730001">
              <Menu.Item>D7730001</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d7730003">
              <Menu.Item>D7730003</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d7730004">
              <Menu.Item>D7730004</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d7730005">
              <Menu.Item>D7730005</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d7730006">
              <Menu.Item>D7730006</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d7730007">
              <Menu.Item>D7730007</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d7730008">
              <Menu.Item>D7730008</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d7730009">
              <Menu.Item active={true}>D7730009</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d8460002">
              <Menu.Item>D8460002</Menu.Item>
            </Link>
            <Link to="/clientnetposition/d8460003">
              <Menu.Item>D8460003</Menu.Item>
            </Link>
            <Link to="/clientnetposition/V7410004">
              <Menu.Item>V7410004</Menu.Item>
            </Link>
          </Menu>
          <Breadcrumb>
            <h2>D7730009</h2>
          </Breadcrumb>
        </Sticky>
        <table className="ui celled table">
          <thead>
            <tr>
              {columns.map((col) => (
                <th key={col}>{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {this.props.data.map((row) => {
              if (row.quantity >= 0) {
                quantity_flag = "positive";
              } else {
                quantity_flag = "negative";
              }
              if (row.quantity !== 0 && row.clientID === "D7730009") {
                return (
                  <tr key={row._id}>
                    <td>{row.clientID}</td>
                    <td>{row.symbol}</td>
                    <td className={quantity_flag}>{row.quantity}</td>
                  </tr>
                );
              }
              return null;
            })}
          </tbody>
        </table>
      </div>
    );
  }
}

const MapStateToProps = (state) => {
  console.log(state);
  let sortedstate = state.NetPositionsData;
  const sorted = {
    data: sortedstate.sort((a, b) => a.clientID.localeCompare(b.clientID)),
  };
  return sorted;
};

const MapDispatchToProps = {
  loadNetPositionsDataSocket: loadNetPositionsDataSocket,
  netpositonsData: netpositonsData,
};

export default connect(MapStateToProps, MapDispatchToProps)(NCP);
