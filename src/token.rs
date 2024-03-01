enum Keywords {
    OpDUP,
    OpDROP,
    OpSWAP,
    OpOVER,
    OpROT,
}

enum Operators {
    Plus,
    Minus,
    GreaterThan,
    LessThan,
    Equal,
    NotEqual,
    Not,
    And,
    Or,
}

enum Delimiters {
    LeftBracket,
    RightBracket,
}

enum Token {
    Keyword(Keywords),
    Operator(Operators),
    Delimiter(Delimiters),
    Number(i32),
    String(String),
}

fn lexer(s: String) -> Vec<Token> {
    let mut tokens: Vec<Token> = Vec::new();
    let mut elems = s.split_whitespace();
    while let Some(e) = elems.next() {
        match e {
            "[" => tokens.push(Token::LeftBracket),
            "]" => tokens.push(Token::RightBracket),
            "+" => tokens.push(Token::Plus),
            "-" => tokens.push(Token::Minus),
            ">" => tokens.push(Token::GreaterThan),
            "<" => tokens.push(Token::LessThan),
            "=" => tokens.push(Token::Equal),
            "<>" => tokens.push(Token::NotEqual),
            "!" => tokens.push(Token::Not),
            "&" => tokens.push(Token::And),
            "|" => tokens.push(Token::Or),
            "DUP" => tokens.push(Token::OpDUP),
            "DROP" => tokens.push(Token::OpDROP),
            "SWAP" => tokens.push(Token::OpSWAP),
            "OVER" => tokens.push(Token::OpOVER),
            "ROT" => tokens.push(Token::OpROT),
            _ => {
                if e.chars().nth(0).unwrap().is_digit(10) {
                    tokens.push(Token::Number(e.parse::<i32>().unwrap()));
                } else {
                    panic!("Invalid token: {}", e);
                }
            }
        }
    }
    tokens
}

enum AstNode {
    Operator(Operators),
    Keyword(Keywords),
    Number(i32),
    Lambda(Vec<AstNode>),
}

fn parser(tokens: Vec<Token>) -> AstNode {
    let mut ast: Vec<AstNode> = Vec::new();
    for t in &mut tokens {
        match t {
            Token::Plus => ast.push(AstNode::Operator(Operators::Plus)),
            Token::Minus => ast.push(AstNode::Operator(Operators::Minus)),
            Token::GreaterThan => ast.push(AstNode::Operator(Operators::GreaterThan)),
            Token::LessThan => ast.push(AstNode::Operator(Operators::LessThan)),
            Token::Equal => ast.push(AstNode::Operator(Operators::Equal)),
            Token::NotEqual => ast.push(AstNode::Operator(Operators::NotEqual)),
            Token::Not => ast.push(AstNode::Operator(Operators::Not)),
            Token::And => ast.push(AstNode::Operator(Operators::And)),
            Token::Or => ast.push(AstNode::Operator(Operators::Or)),
            Token::OpDUP => ast.push(AstNode::Keyword(Keywords::OpDUP)),
            Token::OpDROP => ast.push(AstNode::Keyword(Keywords::OpDROP)),
            Token::OpSWAP => ast.push(AstNode::Keyword(Keywords::OpSWAP)),
            Token::OpOVER => ast.push(AstNode::Keyword(Keywords::OpOVER)),
            Token::OpROT => ast.push(AstNode::Keyword(Keywords::OpROT)),
            Token::Number(n) => ast.push(AstNode::Number(n)),
            Token::LeftBracket => ast.push(parser(tokens)),
            Token::RightBracket => break,
        }
        vec.remove(0);
    }
    AstNode::Lambda(ast);
}
