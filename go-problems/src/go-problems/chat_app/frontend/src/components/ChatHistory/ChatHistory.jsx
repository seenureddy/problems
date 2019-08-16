import React, { Component } from "react";
import "./chathistory.scss";


class ChatHistroy extends Component {

    render() {

        const message = this.props.chatHistory.map((msg, index) =>(
            <p key={index}>{msg.data}</p>
        ));
        return (
            <div className="ChatHistroy">
                <h2> Chat History</h2>
                {message}
            </div>

        );
    }

}

export default ChatHistroy;
