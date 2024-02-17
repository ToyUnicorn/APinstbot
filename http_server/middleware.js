export function requestTime(req, res, next) {
    // req - request
    // res - response
    // next - продолжить выполнение
    req.test = 1;
    next();
}