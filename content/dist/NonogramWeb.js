var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __values = (this && this.__values) || function (o) {
    var m = typeof Symbol === "function" && o[Symbol.iterator], i = 0;
    if (m) return m.call(o);
    return {
        next: function () {
            if (o && i >= o.length) o = void 0;
            return { value: o && o[i++], done: !o };
        }
    };
};
var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
var __spread = (this && this.__spread) || function () {
    for (var ar = [], i = 0; i < arguments.length; i++) ar = ar.concat(__read(arguments[i]));
    return ar;
};
import * as Pako from "pako";
import * as React from "react";
// the nonogram grid should be broken into segments this big by this big for readability.
var GRID_BREAK = 5;
var SquareValue;
(function (SquareValue) {
    SquareValue[SquareValue["CrossedOff"] = 0] = "CrossedOff";
    SquareValue[SquareValue["Empty"] = 1] = "Empty";
    SquareValue[SquareValue["Filled"] = 2] = "Filled";
})(SquareValue || (SquareValue = {}));
var Square = /** @class */ (function (_super) {
    __extends(Square, _super);
    function Square(props) {
        return _super.call(this, props) || this;
    }
    Square.prototype.render = function () {
        var value = this.props.displayValue;
        var buttonContents = value === SquareValue.CrossedOff ? "X" : null;
        var inputProps = {};
        if (value === SquareValue.Filled) {
            inputProps.className = "filled-square";
        }
        else if (value === SquareValue.Empty) {
            inputProps.className = "empty-square";
        }
        else if (this.props.blocked) {
            inputProps.className = "force-blocked-square";
        }
        else {
            inputProps.className = "blocked-square";
        }
        if (this.props.solved || this.props.blocked) {
            inputProps.disabled = true;
        }
        return (React.createElement("button", __assign({ onClick: this.props.onClick }, inputProps), buttonContents));
    };
    return Square;
}(React.Component));
;
var Board = /** @class */ (function (_super) {
    __extends(Board, _super);
    function Board() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Board.prototype.render = function () {
        var e_1, _a, e_2, _b;
        // combine hints and squares into a single array,
        // so that we can cleanly give each row keys.
        // manually track rowIndex so we can use it for modding,
        // and set indices correctly in the ul.
        var rowIndex = 0;
        var board = [];
        var gridStart = this.props.maxLeftHintSize;
        var _loop_1 = function (hintRow) {
            board.push(React.createElement("ul", { className: "board-row", key: rowIndex }, hintRow.map(function (item, itemIndex) {
                var entryClassName;
                if ((itemIndex - gridStart) <= 0 ||
                    itemIndex === (hintRow.length - 1) ||
                    ((itemIndex + 1) - gridStart) % GRID_BREAK !== 0) {
                    entryClassName = "board-entry";
                }
                else {
                    entryClassName = "board-entry-spacer";
                }
                return (React.createElement("li", { className: entryClassName, key: itemIndex },
                    React.createElement(Text, null, item)));
            })));
            rowIndex++;
        };
        try {
            for (var _c = __values(this.props.displayTopHints), _d = _c.next(); !_d.done; _d = _c.next()) {
                var hintRow = _d.value;
                _loop_1(hintRow);
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_1) throw e_1.error; }
        }
        var _loop_2 = function (r, row) {
            // we didn't add spacer rows in the hints because there's no reason to do that.
            // that means our rowIndex is off now and won't space correctly at GRID_BREAK points.
            // so correct for that here.
            var squareRowIndex = rowIndex - this_1.props.maxTopHintSize;
            var rowClassName = void 0;
            if (squareRowIndex === 0 ||
                squareRowIndex === this_1.props.height - 1 ||
                (squareRowIndex + 1) % GRID_BREAK !== 0) {
                rowClassName = "board-row";
            }
            else {
                rowClassName = "board-row-spacer";
            }
            board.push(React.createElement("ul", { className: rowClassName, key: rowIndex },
                this_1.props.displayLeftHints[r].map(function (item, itemIndex) {
                    return (React.createElement("li", { className: "board-entry", key: itemIndex },
                        React.createElement("text", null, item)));
                }),
                row.map(function (item, itemIndex) {
                    var entryClassName;
                    if (itemIndex === (row.length - 1) ||
                        itemIndex % GRID_BREAK !== 0) {
                        entryClassName = "board-entry";
                    }
                    else {
                        entryClassName = "board-entry-spacer";
                    }
                    return (React.createElement("li", { className: entryClassName, key: itemIndex }, item));
                })));
            rowIndex++;
        };
        var this_1 = this;
        try {
            for (var _e = __values(this.props.squares.entries()), _f = _e.next(); !_f.done; _f = _e.next()) {
                var _g = __read(_f.value, 2), r = _g[0], row = _g[1];
                _loop_2(r, row);
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_f && !_f.done && (_b = _e.return)) _b.call(_e);
            }
            finally { if (e_2) throw e_2.error; }
        }
        return board;
    };
    return Board;
}(React.Component));
var Game = /** @class */ (function (_super) {
    __extends(Game, _super);
    function Game(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            code: _this.props.code,
            solved: _this.props.solved,
            validateResult: "No!❌",
            displayLeftHints: [],
            displayTopHints: [],
            leftHints: [],
            topHints: [],
            maxLeftHintSize: 1,
            maxTopHintSize: 1,
            squares: [],
            height: 0,
            size: 0,
            width: 0,
        };
        // TODO I hate this pattern.
        _this.state = _this.decodeSquares(_this.state);
        _this.state = _this.genHints(_this.state);
        _this.state = _this.setBlockedSections(_this.state);
        _this.state = _this.genDisplayHints(_this.state);
        return _this;
    }
    Game.prototype.decodeSquares = function (state) {
        var _this = this;
        var base64Blob = state.code.replace(/_/g, "/").replace(/-/g, "+");
        var zipped;
        try {
            zipped = window.atob(base64Blob);
        }
        catch (err) {
            // TODO more robust error handling.
            // only case we handle now is messed up query params putting an extra ? in.
            var start = base64Blob.indexOf("?");
            zipped = window.atob(base64Blob.slice(0, start));
        }
        // I hate this quote replacing.
        var boardDict = JSON.parse(new TextDecoder("utf-8")
            .decode(Pako.ungzip(zipped)).replace(/'/g, "\""));
        // we need the size separately because the encoding on the other end
        // can lose digits when it encodes the board as a hex string.
        // that SHOULD be redone,
        // but until I get around to it,
        // we have to do this.
        var height = parseInt(boardDict.height, 10);
        var width = parseInt(boardDict.width, 10);
        var size = height * width;
        // okay.
        // so what we're doing here,
        // is reading each hex digit out,
        // converting it to the four squares it represents,
        // and filling those four squares.
        // mapping from a 1D string representing 4-digit chunks to a 2D array,
        // it's weird.
        var hexString = boardDict.squares;
        var i = size - 1;
        var squares = __spread(Array(height).keys()).map(function () { return __spread(Array(width).fill(0)); });
        for (var h = hexString.length - 1; h >= 0; h--) {
            var binChunk = parseInt(hexString[h], 16).toString(2);
            var _loop_3 = function () {
                var filled = binChunk[j] === "1";
                var defaultDisplayValue = void 0;
                if (state.solved && filled) {
                    defaultDisplayValue = SquareValue.Filled;
                }
                else {
                    defaultDisplayValue = SquareValue.Empty;
                }
                var r = Math.floor(i / width);
                var c = i % width;
                squares[r][c] = new Square({
                    "key": i,
                    "filled": filled,
                    "displayValue": defaultDisplayValue,
                    "blocked": false,
                    "onClick": function () { return _this.handleClick(r, c); },
                    "solved": state.solved
                });
                // we may have less squares than the whole hex string would imply.
                i--;
                if (i < 0) {
                    return { value: __assign({}, state, { height: height, width: width, size: size, squares: squares }) };
                }
            };
            for (var j = 3; j >= 0; j--) {
                var state_1 = _loop_3();
                if (typeof state_1 === "object")
                    return state_1.value;
            }
        }
        var _loop_4 = function () {
            var r = Math.floor(i / width);
            var c = i % width;
            squares[r][c] = new Square({
                "key": i,
                "filled": false,
                "displayValue": SquareValue.Empty,
                "blocked": false,
                "onClick": function () { return _this.handleClick(r, c); },
                "solved": state.solved
            });
            i--;
        };
        // final check - we may have a chunk or more at the beginning of hexString that are zeroes.
        // fill out empty squares for this.
        while (i >= 0) {
            _loop_4();
        }
        return __assign({}, state, { height: height, width: width, size: size, squares: squares });
    };
    Game.prototype.genHints = function (state) {
        var e_3, _a, e_4, _b, e_5, _c;
        var leftHints = __spread(Array(state.height).keys()).map(function () { return []; });
        var topHints = __spread(Array(state.width).keys()).map(function () { return []; });
        // calculate max top/left hints as we go,
        // so we don't have to do it later.
        // this is used for formatting the hints.
        // we set to 1 because if we have all empty rows or columns or both,
        // these will never be set.
        var maxTopHintSize = 1;
        var maxLeftHintSize = 1;
        // generate hints by counting squares in each row and column.
        // if we encounter an empty square while having a count,
        // add that as a hint.
        // empty columns are handled in a later step.
        var colCounts = Array(state.width).fill(0);
        try {
            for (var _d = __values(state.squares.entries()), _e = _d.next(); !_e.done; _e = _d.next()) {
                var _f = __read(_e.value, 2), r = _f[0], row = _f[1];
                var rowCount = 0;
                try {
                    for (var _g = __values(row.entries()), _h = _g.next(); !_h.done; _h = _g.next()) {
                        var _j = __read(_h.value, 2), c = _j[0], square = _j[1];
                        if (square.props.filled) {
                            rowCount += 1;
                            colCounts[c] += 1;
                        }
                        else {
                            if (colCounts[c] > 0) {
                                topHints[c].push(colCounts[c]);
                                colCounts[c] = 0;
                                // when pushing new top hints,
                                // check if we have a new largest top hint.
                                if (topHints[c].length > maxTopHintSize) {
                                    maxTopHintSize = topHints[c].length;
                                }
                            }
                            if (rowCount > 0) {
                                leftHints[r].push(rowCount);
                                rowCount = 0;
                                // do this for left hints as well.
                                if (leftHints[r].length > maxLeftHintSize) {
                                    maxLeftHintSize = leftHints[r].length;
                                }
                            }
                        }
                    }
                }
                catch (e_4_1) { e_4 = { error: e_4_1 }; }
                finally {
                    try {
                        if (_h && !_h.done && (_b = _g.return)) _b.call(_g);
                    }
                    finally { if (e_4) throw e_4.error; }
                }
                // handle still having a cell count at end of row.
                if (rowCount > 0) {
                    leftHints[r].push(rowCount);
                    // one more max hint size check.
                    if (leftHints[r].length > maxLeftHintSize) {
                        maxLeftHintSize = leftHints[r].length;
                    }
                }
                // handle empty row.
                if (leftHints[r].length === 0) {
                    leftHints[r].push(0);
                }
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (_e && !_e.done && (_a = _d.return)) _a.call(_d);
            }
            finally { if (e_3) throw e_3.error; }
        }
        try {
            // handle any leftover column counts uncounted due to not finding an empty square.
            for (var _k = __values(colCounts.entries()), _l = _k.next(); !_l.done; _l = _k.next()) {
                var _m = __read(_l.value, 2), c = _m[0], colCount = _m[1];
                if (colCount > 0) {
                    topHints[c].push(colCount);
                    // and one more max hint size check here.
                    if (topHints[c].length > maxTopHintSize) {
                        maxTopHintSize = topHints[c].length;
                    }
                }
                // handle empty columns.
                if (topHints[c].length === 0) {
                    topHints[c].push(0);
                }
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (_l && !_l.done && (_c = _k.return)) _c.call(_k);
            }
            finally { if (e_5) throw e_5.error; }
        }
        return __assign({}, state, { topHints: topHints, leftHints: leftHints, maxLeftHintSize: maxLeftHintSize, maxTopHintSize: maxTopHintSize });
    };
    Game.prototype.setBlockedSections = function (state) {
        var squares = state.squares.map(function (row, r) {
            return row.map(function (square, c) {
                var newProps = __assign({}, square.props);
                if (state.leftHints[r][0] === 0 ||
                    state.topHints[c][0] === 0) {
                    newProps.blocked = true;
                    newProps.displayValue = SquareValue.CrossedOff;
                }
                return new Square(newProps);
            });
        });
        return __assign({}, state, { squares: squares });
    };
    Game.prototype.genDisplayHints = function (state) {
        // we're essentially just padding hints out here.
        // we want all top hints to be arrays of the same length,
        // and we want all left hints to be arrays of the same length.
        // ADDITIONALLY,
        // we want top hints to be padded out by the size of the left hints,
        // so that they align with the board,
        // and,
        // for convenience,
        // we also want the top hints rearranged into rows,
        // not columns.
        var e_6, _a, e_7, _b, e_8, _c;
        var displayLeftHints = [];
        try {
            for (var _d = __values(state.leftHints), _e = _d.next(); !_e.done; _e = _d.next()) {
                var hint = _e.value;
                var newHint = [];
                if (hint.length < state.maxLeftHintSize) {
                    newHint
                        .push.apply(newHint, __spread(Array(state.maxLeftHintSize - hint.length)
                        .fill(null)));
                }
                newHint.push.apply(newHint, __spread(hint));
                displayLeftHints.push(newHint);
            }
        }
        catch (e_6_1) { e_6 = { error: e_6_1 }; }
        finally {
            try {
                if (_e && !_e.done && (_a = _d.return)) _a.call(_d);
            }
            finally { if (e_6) throw e_6.error; }
        }
        var displayTopHints = __spread(Array(state.maxTopHintSize).keys()).map(function () { return Array(state.maxLeftHintSize).fill(null); });
        try {
            for (var _f = __values(state.topHints), _g = _f.next(); !_g.done; _g = _f.next()) {
                var hintCol = _g.value;
                var paddedHintCol = [];
                if (hintCol.length < state.maxTopHintSize) {
                    paddedHintCol.push.apply(paddedHintCol, __spread(Array(state.maxTopHintSize - hintCol.length)
                        .fill(null)));
                }
                paddedHintCol.push.apply(paddedHintCol, __spread(hintCol));
                try {
                    // in addition to padding,
                    // we want to rearrange the top hints from "vertical" arrays to "horizontal",
                    // to make displaying them more straightforward.
                    for (var _h = __values(paddedHintCol.entries()), _j = _h.next(); !_j.done; _j = _h.next()) {
                        var _k = __read(_j.value, 2), h = _k[0], hint = _k[1];
                        displayTopHints[h].push(hint);
                    }
                }
                catch (e_8_1) { e_8 = { error: e_8_1 }; }
                finally {
                    try {
                        if (_j && !_j.done && (_c = _h.return)) _c.call(_h);
                    }
                    finally { if (e_8) throw e_8.error; }
                }
            }
        }
        catch (e_7_1) { e_7 = { error: e_7_1 }; }
        finally {
            try {
                if (_g && !_g.done && (_b = _f.return)) _b.call(_f);
            }
            finally { if (e_7) throw e_7.error; }
        }
        return __assign({}, state, { displayTopHints: displayTopHints, displayLeftHints: displayLeftHints });
    };
    Game.prototype.handleClick = function (r, c) {
        var squares = this.state.squares.slice();
        var square = squares[r][c];
        var displayValue = (square.props.displayValue + 1) % Object.keys(SquareValue).length;
        squares[r][c] = new Square(__assign({}, square.props, { displayValue: displayValue }));
        this.setState({
            squares: squares,
        });
    };
    Game.prototype.validate = function () {
        var e_9, _a, e_10, _b;
        try {
            for (var _c = __values(this.state.squares), _d = _c.next(); !_d.done; _d = _c.next()) {
                var row = _d.value;
                try {
                    for (var row_1 = __values(row), row_1_1 = row_1.next(); !row_1_1.done; row_1_1 = row_1.next()) {
                        var square = row_1_1.value;
                        if ((square.props.filled && square.props.displayValue === SquareValue.Empty) ||
                            (!square.props.filled && square.props.displayValue === SquareValue.Filled)) {
                            return;
                        }
                    }
                }
                catch (e_10_1) { e_10 = { error: e_10_1 }; }
                finally {
                    try {
                        if (row_1_1 && !row_1_1.done && (_b = row_1.return)) _b.call(row_1);
                    }
                    finally { if (e_10) throw e_10.error; }
                }
            }
        }
        catch (e_9_1) { e_9 = { error: e_9_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_9) throw e_9.error; }
        }
        this.setState({
            validateResult: "Yes!✔️",
        });
    };
    Game.prototype.reset = function () {
        var e_11, _a, e_12, _b;
        if (this.state.solved) {
            return;
        }
        var squares = this.state.squares.slice();
        try {
            for (var _c = __values(squares.entries()), _d = _c.next(); !_d.done; _d = _c.next()) {
                var _e = __read(_d.value, 2), r = _e[0], row = _e[1];
                try {
                    for (var _f = __values(row.entries()), _g = _f.next(); !_g.done; _g = _f.next()) {
                        var _h = __read(_g.value, 2), c = _h[0], square = _h[1];
                        var displayValue = void 0;
                        if (square.props.blocked) {
                            displayValue = SquareValue.CrossedOff;
                        }
                        else {
                            displayValue = SquareValue.Empty;
                        }
                        squares[r][c] = new Square(__assign({}, square.props, { displayValue: displayValue }));
                    }
                }
                catch (e_12_1) { e_12 = { error: e_12_1 }; }
                finally {
                    try {
                        if (_g && !_g.done && (_b = _f.return)) _b.call(_f);
                    }
                    finally { if (e_12) throw e_12.error; }
                }
            }
        }
        catch (e_11_1) { e_11 = { error: e_11_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_11) throw e_11.error; }
        }
        this.setState({
            squares: squares,
        });
    };
    Game.prototype.render = function () {
        var _this = this;
        var reset = React.createElement("button", { onClick: function () { return _this.reset(); } }, "Reset");
        var validate = React.createElement("button", { onClick: function () { return _this.validate(); } }, "Validate");
        var gameInfo = null;
        if (this.state.solved === false) {
            gameInfo = (React.createElement("div", { className: "game-info" },
                React.createElement("div", null, reset),
                React.createElement("div", null, validate),
                React.createElement("div", null, this.state.validateResult)));
        }
        return (React.createElement("div", { className: "game" },
            React.createElement("div", { className: "game-board" },
                React.createElement(Board, { squares: this.state.squares, height: this.state.height, width: this.state.width, size: this.state.size, displayTopHints: this.state.displayTopHints, displayLeftHints: this.state.displayLeftHints, maxTopHintSize: this.state.maxTopHintSize, maxLeftHintSize: this.state.maxLeftHintSize })),
            gameInfo));
    };
    return Game;
}(React.Component));
export default Game;
