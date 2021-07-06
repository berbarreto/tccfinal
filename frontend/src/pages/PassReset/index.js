import React from 'react';
import { Link } from 'react-router-dom';

import './styles.css';

export default function PassReset() {

    return (
        <div className="outer-div">
            <div className="entries">
                <div className="inner-div">
                    <img src={process.env.PUBLIC_URL + '/logo.jpeg'} alt="melskin" />
                    <a>We will send an SMS containing your password.</a>
                    <input placeholder="Phone Number" type="tel" required />
                    <button className="send">Send</button>
                    <button className="back">Back</button>
                    <Link className="back-link" to="/login">
                        
                    </Link>
                </div>
            </div>
        </div>
    );

}